%global debug_package %{nil}

Name: haircapture
BuildRequires: SDL-devel
BuildRequires: SDL_ttf-devel
BuildRequires: SDL_gfx-devel
BuildRequires: SDL_image-devel
BuildRequires: smpeg-devel
BuildRequires: libjpeg-devel
BuildRequires: libv4l-devel
BuildRequires: gcc-c++ pkgconfig
License: LGPL
Version: 2.0.0
Release: 70.1
Summary: The C++ object class library for live video handling
# Summary(pt_BR): hairCapture é uma biblioteca de objetos desenvolvida em C++ para manipular vídeo ao vivo. 
Requires: SDL
Requires: SDL_ttf
Requires: SDL_gfx
Requires: SDL_image
Requires: libjpeg
Vendor: Alessandro de Oliveira Faria (A.K.A. CABELO) <alessandrofaria@netitec.com.br>
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Source0: libhaircapture-%{version}.tar.gz 
URL: http://lhaircapture.sourceforge.net

%description 
hairCapture is a C++ object class library for live video handling, using the camera ip and V4L1/2 (Video for Linux version 1) API's calls, for Linux operating system. It's run both in X and console, and live video is displayed by SDL library.

-The current Method of the hairCAPTURE library are:
 + Method LoadBMP (Load image with color Transparent)
 + Method LoadJPG (Load image with Zoom Out)
 + Method Line (Draw Line over video)
 + Method WriteText (Text over video)
 + Added thread for live-video
 + Method SavePPM (save frame)
 + Method SaveJPG (save frame)
 + Player MPEG video file over video live
 + Added suport for V4L2 API
 + Added suport for Camera IP MJPEG (Motion JPEG)
 + Suport for video accelerator 

%description -l pt_BR 
hairCapture é uma biblioteca de objetos desenvolvida em C++ para manipular vídeo ao vivo usando cameras IP e chamadas das API's V4L1/2 Video for Linux versão 1 e 2)do sistema operacional Linux. Esta biblioteca roda no servidor X e modo console, o vídeo é exibido usando a biblioteca SDL.

-Os recustros da biblioteca hairCAPTURE são:
 + Método LoadBMP (Carrega imagens com transparência)
 + Método LoadJPG (Carrega imagens com Zoom Out)
 + Método Line (Desenha uma linha sobre o vídeo ao vivo)
 + Método WriteText (Escreve um texto sobre o vídeo ao vivo)
 + Thread para exibir o vídeo ao vivo.
 + Método SavePPM (salva quadro no formato PPM)
 + Médoto SaveJPG (salva quadro no formato JPG)
 + Reprodução de arquivos MPEG sobre o vidéo ao vivo
 + Compatibilidade com API V4L2
 + Suporte a cameras IP MJPEG (Motion JPEG)
 + Suporte para aceleraçaõ de video

%package devel
Summary: Libraries, includes and more to develop hairCAPTURE applications
Group: Development/Libraries
Requires: %{name}
Requires: SDL-devel
Requires: SDL_ttf-devel
Requires: SDL_gfx-devel
Requires: SDL_image-devel
Requires: smpeg-devel
Requires: libjpeg-devel

%description devel 
hairCapture is a C++ object class library for live video handling, using the camera ip and V4L1/2 (Video for Linux version 1) API's calls, for Linux operating system. It's run both in X and console, and live video is displayed by SDL library.

-The current Method of the hairCAPTURE library are:
 + Method LoadBMP (Load image with color Transparent)
 + Method LoadJPG (Load image with Zoom Out)
 + Method Line (Draw Line over video)
 + Method WriteText (Text over video)
 + Added thread for live-video
 + Method SavePPM (save frame)
 + Method SaveJPG (save frame)
 + Player MPEG video file over video live
 + Added suport for V4L2 API
 + Added suport for Camera IP MJPEG (Motion JPEG)
 + Suport for video accelerator 

%description devel -l pt_BR 
hairCapture é uma biblioteca de objetos desenvolvida em C++ para manipular vídeo ao vivo usando cameras IP e chamadas das API's V4L1/2 Video for Linux versão 1 e 2)do sistema operacional Linux. Esta biblioteca roda no servidor X e modo console, o vídeo é exibido usando a biblioteca SDL.

-Os recustros da biblioteca hairCAPTURE são:
 + Método LoadBMP (Carrega imagens com transparência)
 + Método LoadJPG (Carrega imagens com Zoom Out)
 + Método Line (Desenha uma linha sobre o vídeo ao vivo)
 + Método WriteText (Escreve um texto sobre o vídeo ao vivo)
 + Thread para exibir o vídeo ao vivo.
 + Método SavePPM (salva quadro no formato PPM)
 + Médoto SaveJPG (salva quadro no formato JPG)
 + Reprodução de arquivos MPEG sobre o vidéo ao vivo
 + Compatibilidade com API V4L2
 + Suporte a cameras IP MJPEG (Motion JPEG)
 + Suporte para aceleraçaõ de video

%prep
%setup -q -n lib%{name}-%{version}

%build
%configure --pdfdir=/usr/share/doc/  
%__make %{?jobs:-j%jobs} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
chmod +x $RPM_BUILD_ROOT%{_datadir}/hairCAPTURE-%{version}/build.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/haircapture/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/*

%changelog
* Mon Aug 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuild for Fedora
* Tue Nov 24 2009 13:45:38 Brasil 2009 - alessandrofaria@netitec.com.br - 2.0.0-RC2
- Implementation video accelerator in camera ip and MJPEG format 
* Mon Nov 23 2009 Brasil/East 2009 - alessandrofaria@netitec.com.br - 2.0.0-RC2
- Create package in openSuse Build Alessandro de Oliveira Faria (A.K.A CABELO)
- Update to version 
  + Updated spec file
