%global theme_name    Zukitwo
%global deviantart_id 203936861
%global author        lassekongo83
%global tag           d3df2ot

Name:           zukitwo
Version:        20131210
Release:        2%{?dist}
Summary:        Themes for GTK+2, GTK+3, Metacity, GNOME Shell and Xfwm4
Group:          User Interface/Desktops

License:        GPLv3
URL:            http://%{author}.deviantart.com/art/%{theme_name}-%{deviantart_id}
Source0:        http://www.deviantart.com/download/%{deviantart_id}/%{name}_by_%{author}-%{tag}.zip

# This patch removes two references to Unity-related stuff from 
# Zukitwo/gtk-3.0/gtk.css
Patch0:         %{name}-rm_unity.patch

BuildArch:      noarch      

%description
The %{theme_name} themes for GTK+2, GTK+3, Metacity, GNOME Shell and Xfwm4, 
created by %{author}.


%package common
Summary:        Files common to %{theme_name} themes
Group:          User Interface/Desktops

%description common
Files which are common to all %{theme_name} themes.


%package gtk2-theme
Summary:        %{theme_name} GTK+2 themes
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}, gtk-murrine-engine >= 0.98.1.1, gtk2-engines

%description gtk2-theme
Themes for GTK+2 as part of the %{theme_name} theme.


%package gtk3-theme
Summary:        %{theme_name} GTK+3 themes
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}

%description gtk3-theme
Themes for GTK+3 as part of the %{theme_name} theme.


%package metacity-theme
Summary:        %{theme_name} Metacity themes
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}, metacity

%description metacity-theme
Themes for Metacity as part of the %{theme_name} theme.


%package -n gnome-shell-theme-%{name}
Summary:        %{theme_name} GNOME Shell theme
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}, gnome-shell-extension-user-theme >= 3.10, google-droid-sans-fonts

%description -n gnome-shell-theme-%{name}
%{theme_name} GNOME Shell theme.


%package xfwm4-theme
Summary:        %{theme_name} Xfwm4 themes
Group:          User Interface/Desktops
Requires:       %{name}-common = %{version}-%{release}, xfwm4

%description xfwm4-theme
Themes for Xfwm4 as part of the %{theme_name} theme.


%prep
%setup -q -c -n %{name}_by_%{author}-%{tag}
%patch0 -p0

# Remove "Thumbs.db" files
find . -name Thumbs.db -type f -exec rm -f '{}' \;
# Fix end-of-line encoding of "README"
sed -i 's/\r//' README
# Fix text encoding of "README" 
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README
# Remove Unity stuff
rm %{theme_name}/gtk-3.0/unity.css
rm -r %{theme_name}/unity/
# Remove "index.theme"
rm %{theme_name}/index.theme


%build
# Nothing to build


%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}
cp -pr %{theme_name}/* %{buildroot}%{_datadir}/themes/%{theme_name}
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell
cp -pr %{theme_name}-Shell/gnome-shell/* %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell


%files common
%doc COPYING README
%dir %{_datadir}/themes/%{theme_name}/


%files gtk2-theme
%{_datadir}/themes/%{theme_name}/gtk-2.0/


%files gtk3-theme
%{_datadir}/themes/%{theme_name}/gtk-3.0/


%files metacity-theme
%{_datadir}/themes/%{theme_name}/metacity-1/


%files -n gnome-shell-theme-%{name}
%{_datadir}/themes/%{theme_name}/gnome-shell/


%files xfwm4-theme
%{_datadir}/themes/%{theme_name}/xfwm4/


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20131210-1
- Update to latest upstream version

* Sun Nov 24 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20131107-1
- Update to latest upstream version

* Wed Oct 16 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20131012-1
- Update to latest upstream version (compatible with Gnome >= 3.10)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130424-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20130424-1
- Update to latest upstream version

* Fri Apr 19 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20130418-1
- Update to latest upstream version

* Sat Apr 13 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20130329-1
- Update to latest upstream version (compatible with Gnome >= 3.8)

* Sat Feb 16 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20130207-1
- Update to latest upstream version

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20121216-2
- Correct Spec file

* Sun Jan 13 2013 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20121216-1
- Update to latest upstream version

* Thu Dec 13 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20121211-1
- Update to latest upstream version
- Change font package required by gnome-shell-theme-zukitwo from liberation-sans-fonts to google-droid-sans-fonts

* Sat Dec 08 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20121207-1
- Update to latest upstream version
- Remove everything related to "Zukitwo-Dark"
- Remove fields "Provides" and "Obsoletes"
- Update requirements

* Tue Nov 20 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120817-3
- Add fields "Provides" and "Obsoletes" to the "common" subpackage

* Sun Nov 04 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120817-2
- Package the GNOME Shell theme only for Fedora up to 17

* Fri Aug 17 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120817-1
- Update to latest upstream version

* Sun Aug 05 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120708-5
- Correct an error in .spec file

* Sat Aug 04 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120708-4
- Replace a copy of the directory containing the Gnome Shell theme with a symbolic link to the other 

* Sat Aug 04 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120708-3
- Add a "common" subpackage which owns files and directories that are common to all themes
- Change directory structure

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120708-1
- Update to latest upstream version

* Sat Jul 07 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120702-1
- Update to latest upstream version

* Mon Jun 18 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120612-1
- Update to latest upstream version

* Sat Jun 09 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120607-1
- Update to latest upstream version
- Add a patch to remove "Ubuntu" and "Trebuchet MS" from "font-family" in gnome-shell.css and two references to Unity-related stuff.

* Tue Jun 05 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120602-2
- Add google-droid-sans-fonts as a requirement for gnome-shell-theme-zukitwo
- Add a patch to remove "Ubuntu" from "font-family" in gnome-shell.css

* Sun Jun 03 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120602-1
- Update to latest upstream version
- Change "License" from "GPLv3+" to "GPLv3" in Spec file

* Sat May 26 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120526-1
- Update to latest upstream version

* Fri May 25 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120523-1
- Update to latest upstream version

* Sat May 19 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120516-1
- Update to latest upstream version

* Sat May 12 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 20120511-1
- Initial package for Fedora (thanks to Tim Lauridsen and Mohamed El Morabity for their precious help)
