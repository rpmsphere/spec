Name:           transparent-cursor-theme
BuildArch:      noarch
Summary:        Totally transparent X11 Cursor theme
Version:        0.1.1
Release:        11.1
License:        GPL
Group:          System/X11/Icons
Source:         xcursor-transparent-theme-0.1.1.tar.gz
Patch0:          xcursor-transparent-theme-install-0.1.1.diff
URL:            https://matchbox-project.org/sources/utils/

%description
This package contains a totally transparent X11 Cursor theme. Using
the theme provides an effective and flexible way to hide the X11
Cursor. This kind of behaviour maybe required on Handheld computers
running the X Window System.

Authors:
--------
    Matthew Allum

%prep
%setup -q -n xcursor-transparent-theme-%{version}
%patch 0 -p1

%build
./configure --prefix=/usr --datadir=%{_datadir}

%install
make DESTDIR=%{buildroot} install
mv %{buildroot}%{_datadir}/icons/xcursor-transparent %{buildroot}%{_datadir}/icons/transparent

%files
%{_datadir}/icons/transparent

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
