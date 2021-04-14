Name:           terra
Version:        0.1.5 
Release:        4.1
Summary:        Python/GTK3 drop-down tiling terminal emulator
License:        GPLv3
URL:            https://launchpad.net/terra
Source0:        terra-0.1.5.tar.gz
BuildArch:      noarch
BuildRequires: python2-distutils-extra
BuildRequires: python2 gtk+ pygobject2 vte291
BuildRequires: intltool
Requires: python2 gtk3
Requires: python2-gobject python2-xlib vte291

%description
Terra is GTK+3.0 based terminal emulator with useful user interface, it also
supports multiple terminals with splitting screen horizontally or vertically.
New features will be added soon. It's very new and experimental project.
It's written in python with python-gobject, If you want to contribute just
checkout and try. I really appreciate the bug reports.

%prep
%setup -q

%build
python2 setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root $RPM_BUILD_ROOT --optimize=1

%files
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_docdir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuilt for Fedora
