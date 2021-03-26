Name:           bcnc
Version:        0.9.11git
Release:        6.1
Summary:        GRBL CNC command sender, autoleveler and g-code editor
License:        GPL-2.0+
Group:          Productivity/Graphics/CAD
URL:            https://github.com/vlachoudis/bCNC/
Source0:        bCNC-master.zip
BuildArch:      noarch
Requires:       python2-pyserial
Requires:       python2-enum34

%description
An advanced fully featured g-code sender for GRBL. bCNC is a cross
platform program (Windows, Linux, Mac) written in python. The sender
is robust and fast able to work nicely with old or slow hardware like
Rasperry PI (As it was validated by the GRBL mainter on heavy testing).

%prep
%setup -q -n bCNC-master

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -av * %{buildroot}%{_datadir}/%{name}
install -D -m 0644 bCNC.png %{buildroot}%{_datadir}/pixmaps/bCNC.png

# Create a CLI launcher script
cat > %{buildroot}%{_bindir}/bCNC <<EOF
#!/bin/sh

PYTHONPATH=%{_datadir}/%{name}:%{_datadir}/%{name}/lib:%{_datadir}/%{name}/plugins
export PYTHONPATH

python2 %{_datadir}/%{name}/bCNC.py $*
EOF
chmod 755 %{buildroot}%{_bindir}/bCNC

# Remove some unnecessary files
rm %{buildroot}%{_datadir}/%{name}/bCNC
rm %{buildroot}%{_datadir}/%{name}/bCNC.bat
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/%{name}/bCNC.desktop %{buildroot}%{_datadir}/applications/bCNC.desktop

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/bCNC.py

%files
%{_bindir}/bCNC
%{_datadir}/%{name}
%{_datadir}/applications/bCNC.desktop
%{_datadir}/pixmaps/bCNC.png

%changelog
* Thu Aug 30 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.11git
- Rebuild for Fedora
