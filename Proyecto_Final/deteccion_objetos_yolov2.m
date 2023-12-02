% Detectar Objetos en video mediante YoloV2 preentrenado 
% By Daniel Alvarez Placencia


videoFile = '0-03-20231201231926.mp4';      % Cargar el video
videoReader = VideoReader(videoFile);       % Crear un objeto para leer el video
videoPlayer = vision.DeployableVideoPlayer; % Crear un objeto para ver el video
detector = yolov2ObjectDetector();          % Cargar un detector de objetos con YOLOv2 preentrenado

% % % Funcion % % % 

% analiza cuadro por cuadro
while hasFrame(videoReader)
    % Leer un cuadro del video
    frame = readFrame(videoReader);
    
    % Detectar objetos en el cuadro actual
    [bboxes, scores, labels] = detect(detector, frame);
    
    % Insertar anotaciones en el cuadro para resaltar los objetos detectados
    detectedImg = insertObjectAnnotation(frame, 'rectangle', bboxes, labels);
    
    % Visualizar el cuadro con las anotaciones usando el objeto de visualización
    videoPlayer(detectedImg);
end

% Liberar recursos
release(videoPlayer);

