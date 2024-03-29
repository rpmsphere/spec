#global __spec_install_post %{nil}
#undefine _debugsource_packages
#undefine _missing_build_ids_terminate_build

Summary: An updated version of Sun Microsystems' Fortress programming language
Name: fortress
Version: 1.0
Release: 1
License: BSD
Group: Development/Language
Source0: %{name}-master.zip
URL: https://github.com/pluckyporcupine/fortress
BuildRequires: unzip java-devel-openjdk ant
BuildArch: noarch

%description
This is an effort to update Sun's Fortress programming language to work on Java 9 and, later, Java 10.

%prep
%setup -q -n %{name}-master
sed -i 's|/usr/bin/env python|/usr/bin/python2|' ProjectFortress/astgen/lookup.py
sed -i '/Guessing/d' bin/fortress_home
sed -i 's|egrep|grep -E|' bin/debugOpt bin/fortress_classpath bin/fortress_leaks bin/fortress-old bin/forzip bin/run_classpath bin/runOpt bin/runOptCollect

%build
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
ant clean compile

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
%{_datadir}/%{name}/bin/%{name} "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Jan 14 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
