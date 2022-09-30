%undefine _debugsource_packages

Summary:	Create an APNG from multiple PNG files
Name:		apngasm
Version:	2.91
Release:	3.1
License:	zlib
Group:		Graphics
URL:		http://sourceforge.net/projects/apngasm
Source0:	http://downloads.sourceforge.net/project/apngasm/%{version}/%{name}-%{version}-src.zip
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig

%description
Creates highly optimized Animated PNG files from PNG/TGA image sequences.

%prep
%setup -q -c apnopt

%build
make

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files 
%doc readme.txt 
%{_bindir}/%{name}

%changelog
* Tue Jul 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.91
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.6-3
+ Revision: cad53b1
- MassBuild#464: Increase release tag
