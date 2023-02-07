#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *get_program_name() {
    char szFileName[MAX_PATH];
    GetModuleFileName(NULL, szFileName, MAX_PATH);

    char *fileNameOnly;
    fileNameOnly = strrchr(szFileName, '\\');
    if (fileNameOnly == NULL)
        fileNameOnly = szFileName;
    else
        fileNameOnly++;

    int length = strlen(fileNameOnly);
    char *programName = (char*)malloc((length + 1) * sizeof(char));
    strncpy(programName, fileNameOnly, length);
    programName[length - 4] = '\0';

    return programName;
}

char *get_folder_dir_program() {
    char szFileName[MAX_PATH];
    GetModuleFileName(NULL, szFileName, MAX_PATH);

    char *lastSlash;
    lastSlash = strrchr(szFileName, '\\');
    if (lastSlash == NULL)
        return ".";
    else {
        int length = lastSlash - szFileName + 1;
        char *folderDir = (char*)malloc((length + 1) * sizeof(char));
        strncpy(folderDir, szFileName, length);
        folderDir[length] = '\0';
        return folderDir;
    }
}

char *get_txt_filename(char *programName, char *folderDir) {
    int length = strlen(programName) + strlen(folderDir) + 5;
    char *txtFilename = (char*)malloc((length + 1) * sizeof(char));
    strcpy(txtFilename, folderDir);
    strcat(txtFilename, programName);
    strcat(txtFilename, ".txt");
    return txtFilename;
}

char *get_txt_data(char *txtFilename) {
    FILE *fp;
    fp = fopen(txtFilename, "r");
    if (fp == NULL) {
        printf("No se pudo abrir el archivo %s\n", txtFilename);
        return NULL;
    }

    fseek(fp, 0, SEEK_END);
    int fileSize = ftell(fp);
    rewind(fp);

    char *txtData = (char*)malloc((fileSize + 1) * sizeof(char));
    int bytesRead = fread(txtData, sizeof(char), fileSize, fp);
    if (bytesRead != fileSize) {
        printf("No se pudo leer el archivo completo %s\n", txtFilename);
        free(txtData);
        fclose(fp);
        return NULL;
    }

    txtData[fileSize] = '\0';
    fclose(fp);
    return txtData;
}


void free_memory(char *programName,
                 char *folderDir,
                 char *txtFilename,
                 char *txtData) {
    free(txtData);
    free(txtFilename);
    free(programName);
    free(folderDir);
}

int main(int argc, char* argv[])
{
    char *programName = get_program_name();
    char *folderDir = get_folder_dir_program();
    char *txtFilename = get_txt_filename(programName, folderDir);
    char *txtData = get_txt_data(txtFilename);

    if (txtData == NULL) {
        free_memory(programName, folderDir, txtFilename, txtData);
        return 1;
    }

    int total_length = strlen(txtData);
    for (int i = 1; i < argc; i++) {
        total_length += strlen(argv[i]);
    }

    char *newTxtData = (char*)malloc((total_length + argc + 1) * sizeof(char));
    strcpy(newTxtData, txtData);

    for (int i = 1; i < argc; i++) {
        strcat(newTxtData, " ");
        strcat(newTxtData, argv[i]);
    }
    system(newTxtData);
    free_memory(programName, folderDir, txtFilename, txtData);
    return 0;
}