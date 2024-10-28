%undefine _debugsource_packages

Summary: A dialect of C that looks like Python
Name: brace
Version: 0.9.9
Release: 18.4
License: Public Domain
Group: Development/Language
Source: https://sam.nipl.net/brace/%{name}.tgz
URL: https://sam.nipl.net/cz/
BuildRequires: libpng-devel, SDL-devel, SDL_mixer-devel, mesa-libGL-devel

%description
Brace has coroutines, hygienic macros, header generation, #! scripting and
cached executables, libraries with graphics and sound, and many animated demos.
The newer version is called Cz.

%prep
%setup -q -n %{name}

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
sed -i 's|$(bindir)/br|br|' .build/exe/Makefile
%makeinstall
chmod +x %{buildroot}%{_libdir}/libb.so*
mv %{buildroot}%{_bindir}/br %{buildroot}%{_bindir}/brace_br
mv %{buildroot}%{_bindir}/vib %{buildroot}%{_bindir}/vibrace

%files
%doc copyright !README Changelog Todo Bugs
%{_bindir}/*
%{_includedir}/*
%{_libdir}/bk
%{_libdir}/libb.so*
%{_datadir}/perl5/*

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
