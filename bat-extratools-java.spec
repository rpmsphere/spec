Summary: A collection of extra Java tools for the Binary Analysis Tool
Name: bat-extratools-java
Version: 27.0
Release: 1
URL: http://www.binaryanalysis.org/
License: BSD, public domain
Source0: http://www.binaryanalysis.org/download/fedora/%{name}-%{version}.tar.gz
Group: Development/Tools
BuildRequires: ant
BuildRequires: java-devel-openjdk
BuildRequires: jpackage-utils
Requires: java-openjdk
Requires: jpackage-utils
BuildArch: noarch

%description
A collection of extra Java tools for the Binary Analysis Tool.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
ant

%install
install -D -p -m 644 dedexer/bat-ddx.jar %{buildroot}%{_javadir}/bat-ddx.jar
#install -D -p -m 644 jdeserialize/bat-jdeserialize.jar %{buildroot}%{_javadir}/bat-jdeserialize.jar

%files
%{_javadir}/bat-ddx.jar
#%{_javadir}/bat-jdeserialize.jar

%changelog
* Mon Oct 02 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 27.0
- Update to 27.0

* Wed May 23 2012 Armijn Hemel <armijn@binaryanalysis.org> - 8.0-1
- Update to 8.0
