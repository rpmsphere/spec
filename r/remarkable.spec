%global _name Remarkable

Name: remarkable
Summary: A free fully featured markdown editor
Version: 1.87
Release: 7
Group: Applications/Productivity
License: MIT
URL: https://remarkableapp.github.io/
Source0: https://github.com/jamiemcg/%{_name}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
Requires: python3-beautifulsoup4
Requires: python3-markdown
Requires: wkhtmltopdf
Requires: python3-pdfkit
Requires: gtksourceview3
Requires: webkitgtk4
Patch0: 0003-fixes-184-port-to-WebKit2Gtk.patch
Patch1: 0004-fixes-175-Live-Preview-Mode-Executes-JavaScript.patch

%description
Remarkable has a syntax like Github flavoured markdown. With it you can write
markdown and view the changes as you make them in the live preview window.
You can export your files to a variety of formats. There are multiple styles
available along with extensive configuration options so you can set it up
exactly how you like.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p 1
%patch1 -p 1
sed -i 's|import styles|from remarkable import styles|' %{name}/RemarkableWindow.py

%build

%install
rm -rf %{buildroot}
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{python3_sitelib}
cp -a %{name} %{name}_lib %{buildroot}%{python3_sitelib}
install -d %{buildroot}%{_datadir}/%{name}
cp -a data/* %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Remarkable
Comment=A free, fully featured markdown editor for Linux
Categories=GNOME;Utility;
Exec=remarkable %f
Icon=/usr/share/remarkable/ui/remarkable.png
Terminal=false
Type=Application
EOF

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Sep 09 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.87
- Rebuilt for Fedora
