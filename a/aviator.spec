Summary: A high performance scripting language hosted on the JVM
Name: aviator
Version: 5.3.2
Release: 1
License: LGPLv3
Group: Development/Languages
Source: https://github.com/killme2008/aviatorscript/archive/refs/tags/aviator-%{version}.tar.gz#/aviatorscript-aviator-%{version}.tar.gz
URL: https://github.com/killme2008/aviatorscript
BuildRequires: java-devel-openjdk
BuildRequires: maven
BuildArch: noarch
Requires: jre

%description
AviatorScript is a lightweight, high performance scripting language hosted on
the JVM. It compiles script to java byte code and evaluate it on the fly.

%prep
%setup -q -n aviatorscript-aviator-%{version}

%build
mvn package

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a %{name}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
java \
        -client -XX:+TieredCompilation \
        -Dfile.encoding=UTF-8 \
        -Dmaven.wagon.http.ssl.easy=false \
        -Daviatorscript.original.pwd="\$PWD" \
        -cp %{_datadir}/%{name}/%{name}.jar \
        com.googlecode.aviator.Main "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT
 
%files 
%doc licenses.txt *.md
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.2
- Rebuilt for Fedora
