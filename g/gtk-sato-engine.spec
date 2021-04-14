Name:           gtk-sato-engine
Version:        0.3.1
Release:        19.1
Summary:        Sato GTK Theme Engine
License:        LGPL-2.0
URL:            http://openhand.com
Group:          System/GUI/GNOME
Source0:        http://downloads.yoctoproject.org/releases/sato/sato-engine-%{version}.tar.gz
Source1:        Sato-index.theme
Source2:        http://p1.pichost.me/i/16/1388662.jpg
BuildRequires:  gtk2-devel
Requires:       sato-icon-theme
Requires:       openzone-cursor-theme
Requires:       metacity-themes-compat
Requires:       sato-matchbox-theme

%description
Sato is a reference GTK+/Matchbox based environment aimed primarily at handheld
devices with very high DPI displays. The Sato GTK+ Theme Engine provides the
themeing for GTK+ widgets and is designed for speed and clarity on embedded
hardware.

%prep
%setup -q -n sato-engine-%{version}
cp %{SOURCE1} data/index.theme

%build
%configure
make

%install
%make_install
cp %{SOURCE2} %{buildroot}%{_datadir}/themes/Sato

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING.LIB ChangeLog README NEWS
%{_libdir}/gtk-2.0/*/engines/*.so
%exclude %{_libdir}/gtk-2.0/*/engines/libsato-engine.la
%{_datadir}/themes/Sato

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
