%undefine _debugsource_packages

Name:		ccextractor
Version:	0.93
Release:	1
Summary:	A fast closed captions extractor 
Group:		Video
License:	GPL 2.0
URL:		https://ccextractor.sourceforge.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: utf8proc-devel
BuildRequires: ffmpeg-devel
BuildRequires: tesseract-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: libpng-devel

%description
A fast closed captions extractor for MPEG and H264 files.
Supports DVD, HDTV transport streams, Replay TV. Use this
to create .srt (subtitles) files for your TV captures, 
have transcripts so you can edit subtitles, etc.

%prep
%setup -q

%build
LDFLAGS="-Wl,--allow-multiple-definition -lz -lpng16 -lcrypto"
%ifarch aarch64
export CPPFLAGS=-DPNG_ARM_NEON_OPT=0
%endif
cd linux
./autogen.sh
%configure --enable-ocr --enable-hardsubx
make

%install
rm -rf $RPM_BUILD_ROOT
cd linux
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc docs/*.TXT
%{_bindir}/%{name}

%changelog
* Sun Sep 05 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93
- Rebuilt for Fedora
* Sat Jul 06 2019 tex - 0.88-1pclos2019
- new version
* Fri Nov 22 2013 MBantz <martin dot bantz at gmail dot bantz> 0.67-1pclos2013
- New build
