Summary:	Pluggable Authentication Module for Face based Authentication
Summary(pl.UTF-8):	Modularny system uwierzytelniania PAM opearty o weryfikację twarzy.
Name:		pam_face-authentication
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://www.pam-face-authentication.org
Source0:	http://pam-face-authentication.googlecode.com/files/pam-face-authentication-%{version}-release.tar.gz
#Source0:        pam-face-authentication-master.zip
Source1:	compat.hpp
Patch0:		cmake.patch
BuildRequires:	cmake
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	opencv-devel
BuildRequires:	pam-devel
BuildRequires:	libX11-devel

%description
This is Pluggable Authentication Module for Face based Authentication.

%description -l pl.UTF-8
Modularny system uwierzytelniania PAM opearty o weryfikację twarzy.

%prep
%setup -q -n pam-face-authentication-%{version}-release
#setup -q -n pam-face-authentication-master/qtbranch
%patch0 -p1
#sed -i 's|cv::CascadeClassifier|CascadeClassifier|' include/faceDetector.h
# use cmake file provided by opencv-devel
rm cmake/modules/FindOpenCV.cmake

cp %{SOURCE1} include
sed -i '1i #include "compat.hpp"' src/utils.cpp

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_datadir}/pixmaps

# wtf?
mv $RPM_BUILD_ROOT{%{_prefix}/kde/4/bin,%{_bindir}}/xwindowFaceAuth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog AUTHORS README
%attr(755,root,root) /lib/security/pam_face_authentication.so
%attr(755,root,root) %{_bindir}/qt-facetrainer
%attr(755,root,root) %{_bindir}/xwindowFaceAuth
%{_desktopdir}/qt-facetrainer.desktop
%{_datadir}/haarcascade.xml
%{_datadir}/haarcascade_eye.xml
%{_datadir}/haarcascade_eye_tree_eyeglasses.xml
%{_datadir}/haarcascade_nose.xml
%{_datadir}/pixmaps/pfa-logo.png

%changelog
* Thu Mar 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
