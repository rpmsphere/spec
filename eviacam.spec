Name:		eviacam
Version:	2.1.4git
Release:	1
Summary:	A mouse cursor emulator tracking the users eye movement through a webcam
Group:	        Applications/System
License:	GPLv3+
URL:		https://github.com/cmauri/eviacam
#Source0:	https://github.com/cmauri/eviacam/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:	%{name}-master.zip
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, libv4l-devel, atlas-devel, opencv-devel, libXtst-devel, libXext-devel, gettext, desktop-file-utils
BuildRequires:	wxGTK3-devel
Patch0:         %{name}-2.1.1-fix.patch

%description
eViacam tracks the users eye movement and moves the mouse cursor
accordingly. It provides a GTK user interface for configuration.
It works with any common camera.

%package help
Summary:	Help files for %{name}
BuildArch:	noarch
Requires:	%{name}

%description help
This package contains the help files for %{name}.

%prep
%setup -q -n %{name}-master
%patch0 -p1
#sed -i '1i #include <opencv2/imgproc.hpp>' wxcamwindow/visiblenormroi.cpp

%build
./autogen.sh
%configure --with-wx-config=wx-config-3.0
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc README COPYING AUTHORS ChangeLog INSTALL THANKS TODO
%{_bindir}/%{name}
%{_bindir}/eviacamloader
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/help
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/%{name}*.1.*

%files help
%{_datadir}/%{name}/help

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.4
- Rebuild for Fedora
* Wed Jan 05 2011 Julian Aloofi <julian@fedoraproject.org> 1.4.1-1
- update to version 1.4.1, getting stuff ready for a review request
* Sun Nov 15 2009 Julian Aloofi <julian at, fedoraproject.org> 1.2-1
- update to version 1.2
* Wed Jul 15 2009 Julian Aloofi <julian at, fedoraproject.org> 1.1-2
- fixed the weird file permissions
* Tue Jul 14 2009 Julian Aloofi <julian at, fedoraproject.org> 1.1-1
- Initial package
- some crazy file permissions
