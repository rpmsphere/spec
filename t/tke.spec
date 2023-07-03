Name:		tke
Version:	3.6
Release:	1
Summary:	Advanced Programmer's Editor
License:	GPLv2+
URL:		https://tke.sourceforge.net/
Group:		Editor
Source0:	https://jaist.dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tgz
Source1:        %{name}.desktop
BuildArch:	noarch
Requires:	tcl tclx tcllib tk tklib tkdnd expect

%description
TKE is a full-featured source code editor written in Tcl/Tk with a minimalist UI.

%prep
%setup -q
sed -i '1s|wish8.6|/usr/bin/wish|' scripts/batch_export.tcl
sed -i '1s|tclsh8..|/usr/bin/tclsh|' data/msgs/update.tcl data/msgs/check.tcl scripts/extract_plugin.tcl scripts/uninstall.tcl

%build
cat > %{name}.sh <<EOF
#!/bin/sh
cd /usr/share/tke
wish lib/tke.tcl -name tke -- \$@
EOF

%install
install -Dm755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a data doc lib plugins scripts specl tests %{buildroot}%{_datadir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 data/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README LICENSE ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6
- Rebuilt for Fedora
