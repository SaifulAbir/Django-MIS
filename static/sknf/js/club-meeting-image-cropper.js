$(function () {

  /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
  $("#id_CMF-image").on('change',function () {
  if (this.files && this.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $("#image").attr("src", e.target.result);
      $("#modalPostCrop").modal("show");
    }
    reader.readAsDataURL(this.files[0]);
  }
});

/* SCRIPTS TO HANDLE THE CROPPER BOX */
var $image = $("#image");
var cropBoxData;
var canvasData;
$("#modalPostCrop").on("shown.bs.modal", function () {
  $image.cropper({
    viewMode: 1,
    aspectRatio: 16/9,
    minCropBoxWidth: 200,
    minCropBoxHeight: 200,
    ready: function () {
      $image.cropper("setCanvasData", canvasData);
      $image.cropper("setCropBoxData", cropBoxData);
    }
  });
}).on("hidden.bs.modal", function () {
  cropBoxData = $image.cropper("getCropBoxData");
  canvasData = $image.cropper("getCanvasData");
  $image.cropper("destroy");
});

// Enable zoom in button
$(".js-zoom-in").click(function () {
  $image.cropper("zoom", 0.1);
});

// Enable zoom out button
$(".js-zoom-out").click(function () {
  $image.cropper("zoom", -0.1);
});

  /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
  $(".js-crop-and-upload").click(function () {
    var imageData = $('#image').cropper('getCroppedCanvas').toDataURL() ;
    $('.jcrop-holder').attr('src', imageData);
    $("#id_CMF-image_base64").val(imageData);
    $("#modalPostCrop").modal('hide');
    $("#id_CMF-image").val("");
  });
});