Name:			liquidlnf
Summary:		This is a look and feel for Java GUI applications based on Swing
URL:			https://liquidlnf.dev.java.net/
Group:			Development/Libraries/Java
Version:		0.2.6
Release:		0.3
License:		LGPL
BuildRequires:	ant
BuildRequires:  java-1.6.0-openjdk-devel
BuildRequires:	jpackage-utils >= 1.5
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-resolver
Requires:		java >= 1.5
BuildArch:		noarch
Source:			%{name}-%{version}-src.tar.bz2

%description
This is a look and feel for Java GUI applications based on Swing.

It is based on Mosfet's Liquid 0.9.6-pre4 theme for KDE 3.x. I want
to thanks to Daniel for this great widget theme which I adopted for
use in Java GUI apps. His work is under BSD license.

Author: Miroslav Lazarevic <mickey@birosoft.com>

%package javadoc
Summary:	Javadoc for liquidlnf
Group:		Documentation/HTML

%description javadoc
Javadoc for liquidlnf.

%prep
%setup -q -c -n %{name}

%build
export LANG=de_DE
%ant jar

%javadoc \
	-d doc \
	`find ./ -name \*.java`

%install
%__rm -rf %{buildroot}
# jars
%__install -dm 755 %{buildroot}%{_jvmdir}/jre/lib/ext
%__install -pm 644 dist/%{name}.jar \
	%{buildroot}%{_jvmdir}/jre/lib/ext

%__install -dm 755 %{buildroot}%{_javadir}
%__ln_s %{_jvmdir}/jre/lib/ext/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
#%__install -pm 644 dist/%{name}.jar \
#	%{buildroot}%{_javadir}/%{name}-%{version}.jar
(
cd %{buildroot}%{_javadir}
for jar in *-%{version}*; do
	ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
done
)

%__install -dm 755 %{buildroot}%{_jvmdir}/jre/lib
%__install -m 644 swing.properties \
	%{buildroot}%{_jvmdir}/jre/lib

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

%clean
%__rm -rf %{buildroot}

%post javadoc
%__rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%doc README license.txt
%{_javadir}/*.jar
%{_jvmdir}/jre/lib/*.properties
%{_jvmdir}/jre/lib/ext/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Jan 13 2009 Feather Mountain <john@ossii.com.tw> - 0.2.6-0.3.ossii
- Rebuild for M6(OSSII)
* Tue Feb 20 2007 Toni Graffy <toni@links2linux.de> - 0.2.6-0.pm.3
- installed liquidlnf in /usr/lib/jvm/jre/lib/ext to avoid breaking other java-apps
- added javadoc-subpackage
* Wed Dec 27 2006 Toni Graffy <toni@links2linux.de> - 0.2.6-0.pm.2
- build SuSE-10.2, corrected BuildRequires
* Sun Sep 17 2006 Toni Graffy <toni@links2linux.de> - 0.2.6-0.pm.1
- build for packman
* Sun Jul 02 2006 oc2pus <oc2pus@arcor.de> - 0.2.6-0.oc2pus.1
- First packaged release 0.2.6
