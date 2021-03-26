Name: nubasic
Summary: BASIC language interpreter written in C++11 for educational purposes
Version: 1.51
Release: 1
Group: Development/Language
License: GPLv2+
URL: http://www.nubasic.eu
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}-rel_%{version}.tar.gz
BuildRequires: libX11-devel
BuildRequires: xterm xorg-x11-apps

%description
nuBASIC has been designed mainly for educational purposes both for C++ developers that
can deal with a non-trivial example of C++11 programming and for nuBASIC's users,
that may get hooked on programming.
As the name suggests, nuBASIC is a programming language from the BASIC family.
Anyone who has previously worked with other BASIC languages will quickly become accustomed to nuBASIC.
Large sections of the basic constructs of nuBASIC are compatible with other Basic dialects.
nuBASIC can be used by any user without any additional programs.
It has the components needed to create programs, including:
- The command line interpreter (CLI), which provides an inline-editor for creating and testing programs.
- The language interpreter, which is needed to run nuBASIC programs

%prep
%setup -q -n %{name}-rel_%{version}
sed -i 's|-Wall|-Wall -fPIC|' CMakeLists.txt
sed -i '9i #include <string>' lib/nu_playsnd.cc

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog README NEWS THANKS
%{_bindir}/%{name}*
#{_libdir}/lib%{name}.a

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.51
- Rebuild for Fedora
* Thu Sep 11 2014 Fedora 20 Release <acaldmail@gmail.com> - 1.19
- Rebuild RPM for Fedora distros
