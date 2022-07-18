Name:		finalterm
Summary:	Terminal emulator
Version:	0.1
Release:	8.1
License:	GPLv3
Group:		User Interface/Desktops
URL:		http://finalterm.org/		
Source0:	%{name}-master.zip
BuildRequires:	cmake gcc-c++ libstdc++-devel libgee-devel gnome-common gtk-doc gtk3-devel libmx-devel
BuildRequires:	clutter-gtk-devel keybinder-devel intltool
BuildRequires:  vala-compat-devel vala-compat vala-compat-tools
BuildRequires:	keybinder3-devel w3m

%description
Final Term is an terminal is a new breed of terminal emulator.
It goes beyond mere emulation and understands what is happening inside the shell it is hosting.
This allows it to offer features no other terminal can, including:
* Semantic text menus
* Smart command completion
* GUI terminal controls

%prep
%setup -q -n %{name}-master
cp data/%{name}.desktop.in data/%{name}.desktop
sed -i 's|menu, out x, out y|menu, ref x, ref y|' src/TerminalView.vala

%build
%cmake .
%cmake_build

%install
%cmake_install

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.finalterm.gschema.xml
%{_datadir}/icons/hicolor/*/apps/final-term.*
%{_datadir}/locale/*/LC_MESSAGES/finalterm.mo
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Wed May 8 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 1.0-1
- initial packaging
