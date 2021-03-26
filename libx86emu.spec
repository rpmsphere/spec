# el6 compatibility
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"

Name:           libx86emu
Version:        3.1
Release:        1
Summary:        x86 emulation library
License:        BSD
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libx86emu-1.11-ldflags.patch
BuildRequires:  gcc

%description
Small x86 emulation library with focus of easy usage and extended execution
logging functions. The library features an API to create emulation objects
for x86 architecture.

%package devel
Summary:        Development files for libx86emu
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing with libx86emu, a x86 emulation
library.

%prep
%setup -q

%build
%make_build %{make_flags} shared

%ldconfig_scriptlets

%install
%make_install %{make_flags}

%files
%{_libdir}/libx86emu.so.*
%doc README.md
%license LICENSE

%files devel
%{_includedir}/x86emu.h
%{_libdir}/libx86emu.so

%changelog
* Fri Feb 14 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuild for Fedora
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Dec 20 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.11-7
- Bump release to rebuild
* Tue Dec 18 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.11-6
- Fix missed __global_ldflags on el6
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.11-3
- Properly apply build flags
* Fri Aug 25 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.11-2
- Better align with packaging guidelines (thanks Robert-André Mauchin)
* Tue Aug 01 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.11-1
- Initial packaging
