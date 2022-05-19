%undefine _debugsource_packages

Summary: A modern replacement for the autoconf and make tools
Name: makeme
Version: 1.0.5
Release: 1
License: Dual GPL/commercial
Group: Development/Other
URL: http://embedthis.com/makeme
#SOURCE0: https://s3.amazonaws.com/embedthis.software/%{name}-%{version}-src.tgz
SOURCE0: https://github.com/embedthis/makeme/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
MakeMe is a replacement for the autoconf/make build tools. MakeMe is a
single tool that configures, builds and generated native build projects
for applications. It expresses build rules in the JavaScript language.

%prep
%setup -q

%build
#configure
#make_build
make boot

%install
#make install
install -d %{buildroot}%{_libdir}/%{name}
cp -a build/linux-*-release/bin/* %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_includedir}/%{name}
install build/linux-*-release/inc/* %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_bindir}
ln -s ../%{_lib}/%{name}/me %{buildroot}%{_bindir}/%{name}

%files
%doc *.md doc/*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_includedir}/%{name}

%changelog
* Sun Apr 17 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuilt for Fedora
