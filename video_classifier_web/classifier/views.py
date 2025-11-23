from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Video
from .forms import VideoForm
from .utils import predict_video


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            
            # ✅ Run Model Prediction
            pred_class, conf = predict_video(video.video_file.path)
            
            video.prediction = pred_class
            video.confidence = round(conf, 2)
            video.save()

            messages.success(request, "✅ Video uploaded & analyzed successfully!")
            return redirect('video_list')
    else:
        form = VideoForm()

    return render(request, 'upload.html', {'form': form})


def video_list(request):
    # ✅ Filtering videos
    filter_option = request.GET.get('filter', 'all')

    if filter_option == 'theft':
        videos = Video.objects.filter(prediction="Theft")
    elif filter_option == 'safe':
        videos = Video.objects.filter(prediction="Safe")
    else:
        videos = Video.objects.all()

    videos = videos.order_by('-uploaded_at')

    return render(request, 'video_list.html', {
        'videos': videos,
        'filter_option': filter_option
    })


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video_detail.html', {'video': video})


def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        video.delete()
        messages.success(request, "🗑 Video deleted successfully!")
        return redirect('video_list')

    return render(request, 'confirm_delete.html', {'video': video})
