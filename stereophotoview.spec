Name:		stereophotoview
Version:	1.13.0
Release:	1
Summary:	Viewer/editor for stereoscopic 3d photo and video
URL:		https://stereophotoview.bitbucket.io
License:	GPLv3
Group:		Graphics
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}_autolayout.patch
Patch1:		%{name}_patch.diff 
Patch2:		%{name}_lib.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(gl)
BuildRequires:	ffmpeg-devel
BuildRequires:	qt5-linguist
BuildRequires:	shared-mime-info

%description
StereoPhotoView is a viewer/editor for stereoscopic 3d photo and video.

%prep
%setup -q
%patch0  -p0
#patch1 -p1
#patch2 -p0

%build
%qmake_qt5 LIB=%{_lib} PREFIX=%{buildroot}/usr
%make_build

%install
%make_install

%files
%doc README* COPYING
%{_bindir}/%{name}
%{_bindir}/stereo-conv
%{_datadir}/applications/stereophotoview.desktop
%{_iconsdir}/hicolor/scalable/apps/stereophotoview.svg
%{_libdir}/libstereophotoview.so.*

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13.0
- Rebuild for Fedora
* Sun Jul 15 2018 User <user@mail.net> 1.11.0-2
- (954420d) Update spec, fixed issue1, release 2
