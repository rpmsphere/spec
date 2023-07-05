Name: flvtool++
Version: 1.2.1
Release: 1
Summary: A command line Flash Video file (FLV) editor
Summary(ru_RU.UTF8): flvtool++ утилита для манипуляций с метаданными файлов Macromedia Flash Video (FLV)
License: BSD 
Group: Applications/File
URL: https://bramp.net/blog/2006/06/flvtool-a-command-line-flash-video-file-flv-editor/
Source: https://repo.bstack.net/flvtool++/%{name}-%{version}.tar.gz
BuildRequires: python2-scons gcc-c++ boost-devel

%description
flvtool++ is a tool for hinting and manipulating the metadata of
Macromedia Flash Video (FLV) files. It was originally created for
Facebook's Video project (https://facebook.com/video/) for fast video
hinting. It is loosely based on the Ruby FLVTool2, but is written in
C++ for performance reasons.

%description -l ru_RU.UTF8
flvtool++ утилита для манипуляций с Macromedia Flash Video files (FLV).
Она может работать с множеством метаданных. Изначально была создана  для
видео-проекта Facebook и базируется на FLVTool2, но переписана с Ruby на
C++ для повышения производительности.

%prep
%setup -q -c

%build
scons

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGELOG LICENSE README
%_bindir/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuilt for Fedora
* Wed Dec 23 2009 Sergey Alembekov <rt@altlinux.ru> 1.2.1-alt1
- initial build
