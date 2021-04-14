%undefine _debugsource_packages

Name:		qtagconvert
Version: 2.0.0
Release: 5.1
License:	GPL
Source:		%{name}-%{version}.tar.bz2
Vendor:		drmoriarty.0@gmail.com
Group:		Multimedia
Summary:	MP3 tag converter
BuildRequires:	gcc-c++, sed, taglib-devel, pkgconfig(QtGui)

%description
Tag editor for mp3 files. Designed to convert codepage for ID3v1 and ID3v2 tags.

%prep
%setup -q
sed 's/Version=2.0.0/Version=1.0/' %{name}.desktop
sed 's/Encoding=UTF-8//' %{name}.desktop
sed 's/Categories=AudioVideo;/Categories=AudioVideo;Audio;AudioVideoEditing;Qt;/' %{name}.desktop

%build
qmake-qt4
lrelease-qt4 %{name}.pro
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-2.0.0

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc COPYING README.utf8
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
* Sun Feb 06 2011 Petr Vanek <petr@scribus.info> 0.5
- suse fixes
* Tue May 19 2009 TI_Eugene <ti.eugene@gmail.com> 0.5
- Initial build in OBS
