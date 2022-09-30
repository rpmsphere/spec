%undefine _debugsource_packages
%global _name x10

Name: x10lang
Summary: X10 Programming language compiler and Runtime
Version: 2.6.2
Release: 1
Group: Development/Programming
License: Eclipse Public Licence
URL: http://x10-lang.org
Source0: http://downloads.sourceforge.net/project/%{_name}/%{_name}/%{version}/%{_name}-%{version}-src.tar.bz2
BuildRequires: java-devel-openjdk
BuildRequires: lua
BuildRequires: ant
Source1: x10-local-jar.zip
Requires: java

%description
X10 is a programming language that aims to make you 10 times more productive when programming modern computers,
from multi-core desktops, to GPUs, on up to large clusters with thousands of processors.  If you are familiar
with C++ or Java, then you'll quickly become comfortable with the basic syntax of X10.  On top of that, we add
features that make expressing computational parallelism, and the movement of data across memory spaces, as
elegant as standard sequential program features.  X10 developers have access to a full eclipse-based IDE called
X10DT, and a community of developers to help you get started.

%prep
%setup -q -c
unzip %{SOURCE1}
sed -i 's|/include|/../include|g' x10.runtime/Make.rules
cp /usr/lib/jvm/java-openjdk/include/jni.h /usr/lib/jvm/java-openjdk/include/linux/jni_md.h x10.runtime/x10rt/include/

%build
cd x10.dist
ant -Doptimize=true dist-java dist-cpp

%install
mkdir -p %{buildroot}/opt/%{_name} %{buildroot}%{_bindir}
cp -a x10.dist/* %{buildroot}/opt/%{_name}
cd x10.dist/bin
for i in * ; do
ln -s /opt/%{_name}/bin/$i %{buildroot}%{_bindir}/$i
done

%files
%{_bindir}/*
/opt/%{_name}

%changelog
* Thu Sep 12 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.2
- Rebuilt for Fedora
