%undefine _debugsource_packages
%define oname   mvc
%define oversion 2015-05-08
%define pversion 2015_05_08

Summary:        Convert almost any video 
Name:           mirovideoconverter
Version:        3.0.2
Release:        4.1
URL:            https://www.mirovideoconverter.com/
Source0:        https://nightlies.pculture.org/data_volume/%{oname}-%{oversion}-.tar.gz
Patch0:         linux-build.patch
License:        GPLv3
Group:          Video
BuildRequires:  pkgconfig(python)
BuildRequires:  python2-setuptools
BuildRequires:  desktop-file-utils
Requires:       python(abi)
Requires:       ffmpeg
BuildArch:      noarch

%description
Miro Video Converter is super simple way to
convert almost any video to MP4, WebM (vp8), 
Ogg Theora, or for Android, iPhone, and more.

%prep
%setup -q
rm -fr setup-files/osx
rm -fr setup-files/windows
%patch 0 -p0

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} 

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files 
%doc LICENSE 
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Mon Jul 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.2-2.2015_05_08
- Rebuilt for Fedora
* Sun Nov 15 2015 Denis Silakov <dsilakov@gmail.com> 3.0.2-2.2015_05_08
- (e7a69d3) Updated to 2015-05-08 snapshot
