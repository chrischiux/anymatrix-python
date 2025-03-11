% function export_to_json()
%     % Capture multiple outputs from anymatrix using a cell array
%     index = anymatrix("sets", "test_set");

%     numMatrix = length(index);
%     disp(numMatrix);

%     [varargout{1:numMatrix}] = anymatrix("sets", "test_set");

%     % Create a cell array to hold all matrices
%     matrices = cell(1, numMatrix-1);
%     for i = 1:numMatrix-1
%         matrices{i} = varargout{i+1};
%     end

%     % Convert the cell array to a JSON string
%     jsonString = jsonencode(matrices);

%     % Write the JSON string to a file
%     fileID = fopen('output.json', 'w');
%     if fileID == -1
%         error('Cannot open file for writing.');
%     end
%     fprintf(fileID, '%s', jsonString);
%     fclose(fileID);
% end

function export_to_json()
    % Capture multiple outputs from anymatrix using a cell array
    index = anymatrix("sets", "test_set");

    numMatrix = length(index);
    disp(numMatrix);

    [varargout{1:numMatrix}] = anymatrix("sets", "test_set");

    % Create a cell array to hold all matrices
    matrices = cell(1, numMatrix-1);
    for i = 1:numMatrix-1
        matrices{i} = varargout{i+1};
    end

    % Create a structure array to hold all matrices with the key "matrix"
    matrixStructArray = cell(numMatrix-1);
    for i = 1:numMatrix-1
        matrixStructArray{i} = struct('matrix_ID', index{i,1},'parameters', index{i,2} , 'matrix', matrices{i});
    end

    % Convert the structure array to a JSON string
    jsonString = jsonencode(matrixStructArray, PrettyPrint=true);

    % Write the JSON string to a file
    fileID = fopen('output.json', 'w');
    if fileID == -1
        error('Cannot open file for writing.');
    end
    fprintf(fileID, '%s', jsonString);
    fclose(fileID);
end