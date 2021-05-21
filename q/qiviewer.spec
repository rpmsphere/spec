Name:		qiviewer
Version:	0.7.0git
Release:	1
Summary:	Qt-based lightweight image viewer
License:	GPL
Source0:	%{name}-master.zip
Source1:	%{name}.desktop
Group:		Productivity/Graphics/Viewers
URL:            https://github.com/samkpo/qiviewer
BuildRequires:	gcc-c++, qt4-devel

%description
This program has been written with help of Qt library, to be a lightweight
image viewer, similar to eog or viewnior for Gnome Supported formats:
BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, XBM, XPM.

%prep
%setup -q -n %{name}-master

%build
%cmake .
%cmake_build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%cmake_install
mv $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jan 06 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0git
- Rebuilt for Fedora
* Fri May 20 2011 TI_Eugene <ti.eugene@gmail.com> 0.5
- next version
* Tue Apr 26 2011 Petr Vanek <petr@scribus.info> 0.4
- version bump
* Fri Jan 07 2011 TI_Eugene <ti.eugene@gmail.com> 1.0beta
- initial package in OBS
