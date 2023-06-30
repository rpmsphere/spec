Name:		firebox-tools
Version:	0.5.0
Release:	1
Summary:	Tools for the Firebox Window Manager
Group:		User Interface/Desktops
License:	GPLv2+
URL:		https://firebox.intuxication.org/
Source:		https://download.gna.org/firebox/tarballs/%{name}-%{version}.tar.gz
Source1:	%{name}-0.5.0.zh_TW.po
Requires:	gtk2, libxml2, firebox
BuildRequires:	gtk2-devel, libxml2-devel

%description
Tools for the Firebox Window Manager.

%prep
%setup -q
sed -i 's/fr/fr zh_TW/' po/LINGUAS
cp %{SOURCE1} po/zh_TW.po
msgfmt po/zh_TW.po -o po/zh_TW.gmo
sed -i 's|glib/g.*\.h|glib.h|' src/xml.h

%build
%configure

%install
rm -rf %{buildroot}
%makeinstall

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/fbconf
%{_datadir}/%{name}/theme_default.png
%{_mandir}/man1/fbconf.1.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
