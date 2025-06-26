import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, Image, X } from 'lucide-react';

const ImageUploader = ({ onImageSelect, imagePreview }) => {
  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file) {
      onImageSelect(file);
    }
  }, [onImageSelect]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp']
    },
    multiple: false,
    maxSize: 10 * 1024 * 1024 // 10MB
  });

  const handleRemoveImage = (e) => {
    e.stopPropagation();
    onImageSelect(null);
  };

  return (
    <div className="w-full">
      {!imagePreview ? (
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-200 ${
            isDragActive 
              ? 'border-primary-500 bg-primary-50' 
              : 'border-gray-300 hover:border-primary-400 hover:bg-gray-50'
          }`}
        >
          <input {...getInputProps()} />
          <div className="flex flex-col items-center space-y-4">
            <div className="p-4 bg-gray-100 rounded-full">
              <Upload className="w-8 h-8 text-gray-600" />
            </div>
            <div>
              <p className="text-lg font-medium text-gray-700">
                {isDragActive ? 'Drop your image here' : 'Drag & drop an image here'}
              </p>
              <p className="text-sm text-gray-500 mt-1">
                or click to browse • Supports JPG, PNG, GIF, WebP • Max 10MB
              </p>
            </div>
          </div>
        </div>
      ) : (
        <div className="relative group">
          <div className="rounded-xl overflow-hidden border border-gray-200 shadow-sm">
            <img
              src={imagePreview}
              alt="Preview"
              className="w-full h-64 object-cover"
            />
          </div>
          <button
            onClick={handleRemoveImage}
            className="absolute top-3 right-3 p-2 bg-red-500 text-white rounded-full hover:bg-red-600 transition-colors duration-200 opacity-0 group-hover:opacity-100"
            title="Remove image"
          >
            <X className="w-4 h-4" />
          </button>
          <div className="absolute bottom-3 left-3 bg-black bg-opacity-50 text-white px-3 py-1 rounded-lg text-sm">
            <Image className="w-4 h-4 inline mr-2" />
            Image uploaded
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
