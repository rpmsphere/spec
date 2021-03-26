%global debug_package %{nil}

Name:		radiola
Version:	0.0.1
Release:	6.1
License:	GPL
Vendor:		Socolov
Source:		trunk-%{version}.tar.bz2
Group:		Productivity/Graphics/Viewers
Summary:	Lightweight Internet Radio
BuildRequires:	gcc-c++, cmake, hicolor-icon-theme, pkgconfig(QtGui)
Requires:	mplayer

%description
Please download any *.pls (e.g. http://somafm.com/play/groovesalad130),
put it to ~/.config/radiola/playlist.pls, run radiola and select any channel.

%prep
%setup -n trunk-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/radiola.png
%{_datadir}/%{name}

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
* Tue Dec 20 2011 TI_Eugene <ti.eugene@gmail.com> - 0.0.1
- initial OBS revision
