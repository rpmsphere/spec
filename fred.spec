Name:		fred
Version:	0.7.5.1458
Release:	13.1
Summary:	Freenet REference Daemon
License:	GPLv2
Group:		System/Daemons
#Source0:	https://github.com/freenet/fred-official/archive/build01458.tar.gz
Source0:	%{name}-official-build01458.tar.gz
Source1:	http://freenet.googlecode.com/files/freenet-ext.jar.29
Source2:	http://www.bouncycastle.org/download/bcprov-jdk15on-150.jar
URL:		https://freenetproject.org/
BuildRequires:	java-devel-openjdk lua
BuildRequires:	xml-commons-apis
BuildRequires:	ant
#BuildRequires:	ant-junit
Requires:	jre
BuildArch:	noarch

%description
Share files, chat on forums, browse and publish, anonymously and without fear of
blocking or censorship! Then connect to your friends for even better security!

%prep
%setup -q -n %{name}-official-build01458
cp %{SOURCE1} lib/freenet/freenet-ext.jar
cp %{SOURCE2} lib/bcprov.jar
sed -i 's|unit, ||' build-clean.xml

%build
%ant

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a dist/* %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd /usr/share/%{name}
java -jar freenet.jar
EOF

%files
%doc README.* LICENSE AUTHORS
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Jan 14 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5.1458
- Rebuild for Fedora
