Summary:	High-level audio API
Name:		audiere
Version:	1.9.4
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://audiere.sourceforge.net
Source:		http://prdownloads.sourceforge.net/audiere/%{name}-%{version}-src.tar.bz2
Patch0:		%{name}-1.9.4-speex.patch
Patch1:		%{name}-1.9.4-gcc43.patch
Patch2:		%{name}-1.9.4-flac.patch
Patch3:		audiere-1.9.4-add-missing-header.patch
BuildRequires:	audiofile-devel
BuildRequires:	flac-devel
BuildRequires:	libcdaudio-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	speex-devel

%description
Audiere is a high-level audio API. It can play Ogg Vorbis, MP3,
FLAC, uncompressed WAV, AIFF, MOD, S3M, XM, and IT files. For
audio output, Audiere supports DirectSound or WinMM in Windows,
OSS on Linux and Cygwin, and SGI AL on IRIX.

%package devel
Summary:	Development headers and libraries for audiere
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}
Requires:	flac-devel
Requires:	libcdaudio-devel
Requires:	libogg-devel
Requires:	libvorbis-devel
Requires:	speex-devel

%description devel
Development headers and libraries for audiere.

%prep
%setup -qn audiere
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's|MIDIDeviceDialog::OnButton|OnButton|' examples/wxPlayer/MIDIDeviceDialog.h
sed -i 's| wxString(| wxString::FromAscii(|' examples/wxPlayer/DeviceFrame.cpp
sed -i 's|wxOPEN|wxFD_OPEN|' examples/wxPlayer/DeviceFrame.cpp examples/wxPlayer/MIDIDeviceFrame.cpp

%build
sh ./bootstrap
%configure --enable-opt --enable-unicode
make

%install
%makeinstall
rm %{buildroot}%{_libdir}/lib*.la

%clean
rm -rf %{buildroot}

%files
%{_libdir}/libaudiere-%{version}.so

%files devel
%doc doc/*.txt
%{_bindir}/wxPlayer
%{_bindir}/audiere-config
%{_includedir}/audiere.h
%{_libdir}/libaudiere.a
%{_libdir}/libaudiere.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.4
- Rebuild for Fedora
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.4-10mdv2011.0
+ Revision: 610005
- rebuild
* Sat Feb 13 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-9mdv2010.1
+ Revision: 505582
- Patch3: add missing header
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.9.4-7mdv2009.0
+ Revision: 266224
- rebuild early 2009.0 package (before pixel changes)
* Tue Jun 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-6mdv2009.0
+ Revision: 214779
- Patch0: fix compilation against speex
- Patch1: fix compilation against gcc-4.3
- Patch2: fix compilation against flac
- fix provides for devel library
* Sun Mar 09 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-5mdv2008.1
+ Revision: 183136
- new license policy
* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.9.4-4mdv2008.1
+ Revision: 170768
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.9.4-3mdv2008.0
+ Revision: 67948
- fix description
* Sun Aug 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-2mdv2008.0
+ Revision: 66520
- add more provides on devel package
* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.4-1mdv2008.0
+ Revision: 44190
- Import audiere
