%global debug_package %{nil}
Name:		firebox
Version:	0.5.0
Release:	1
Summary:	Firebox is yet another Window Manager for X11 systems.
Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://firebox.intuxication.org/
Source:		http://download.gna.org/firebox/tarballs/%{name}-%{version}.tar.gz
Source1:	%{name}-0.4.0.zh_TW.po
BuildRequires:  libxml2-devel
BuildRequires:  libpng12-devel
BuildRequires:	libXcomposite-devel

%description
Still in development, it is not forked from Openbox, Fluxbox, Blackbox or
even Hackedbox ; it is written from scratch, in C langage.

Its goal is not to be a Desktop Manager (ie no pager nor toolbar) but
- for instance - something between Openbox and wmii: small, quite fast,
eye candy and keyboard oriented, with some orginal features.

%prep
%setup -q
sed -i 's/fr/fr zh_TW/' po/LINGUAS
cp %{SOURCE1} po/zh_TW.po
msgfmt po/zh_TW.po -o po/zh_TW.gmo
sed -i 's|libpng |libpng12 |' configure*

%build
autoreconf -ifv
%configure
sed -i -e 's|libpng16|libpng12|' -e 's|-lX11|-lX11 -lm|' -e 's|-Wall|-Wall -fPIC|' Makefile */Makefile
make

%install
rm -rf %{buildroot}
%makeinstall
gzip %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}/schemas/theme.xsd

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuild for Fedora
