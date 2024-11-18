%undefine _debugsource_packages

Name:           jd4x
Version:        0.6
Release:        2
Summary:        Java Desktop for X Window
Group:          User Interface/Desktops
License:        GPL
URL:            https://jdx.sourceforge.net/
Source0:        https://jaist.dl.sourceforge.net/project/jdx/Documentation%20%28JD4X%20Core%29/jd4x-stable-v%{version}/%{name}-src.tar.gz   
#BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-devel
BuildRequires: lua
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: libXext-devel
BuildRequires: libXaw-devel

%description
JD4X is a completely Java orientated desktop for Linux x86 X Window users.
It is aimed at Java users and developers who desires a truely Java friendly
desktop that supports both native and Java applications. Visit our project
website for more details.

%prep
%setup -q -n %{name}
sed -i -e 's|JDK=.*|JDK=/usr/lib/jvm/java/include|' -e 's|CFLAGS=.*|CFLAGS=-O2 -fPIC -Wno-return-mismatch -Wno-implicit-function-declaration|' -e 's|-static||' linux/makefile moth/makefile
sed -i 's|${JCH}.*|javac -classpath ${BUILD} -h ${INC} *.java|' linux/makefile moth/makefile
sed -i '33i #include <string.h>' moth/window.c

%build
make all misc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -a build/%{name} $RPM_BUILD_ROOT%{_libdir}

%files
%doc SUPPORT COPYING
%{_libdir}/%{name}

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
