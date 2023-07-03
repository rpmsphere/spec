Name: zhspeak
License: GPL
Group: Application/Multimedia
Summary: A text-to-speech (TTS) software
Version: 2.1.0
Release: 1
#Source: https://nchc.dl.sourceforge.net/sourceforge/e-guidedog/%{name}-%{version}_generic.7z
Source: %{name}-%{version}_generic.tgz
URL: https://e-guidedog.sourceforge.net/zhspeak.php
BuildArch: noarch
Requires: python3 vorbis-tools

%description
This is a lightweight Chinese TTS, which uses the same voice files to Ekho.
It has smaller package size (WAVE voice files are compressed in OGG format)
and easier to install (written in Python).

%prep
%setup -q -c
#sed -i 's/python3/python/' bin/%{name}.py

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/%{name}
cp -a * %{buildroot}/%{_datadir}/%{name}
cat > %{buildroot}/%{_bindir}/%{name} << EOF
#!/bin/sh
%{_datadir}/%{name}/bin/%{name}.py "\$@"
EOF

%clean
%__rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
