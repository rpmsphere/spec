Name:               mruby
Version:            3.0.0
Release:            1
Summary:            Lightweight Ruby
Source:             %{name}-%{version}.tar.gz
URL:                https://github.com/mruby/mruby/
Group:              Development/Languages/Ruby
License:            MIT
BuildRequires:      bison
BuildRequires:      ruby rubypick rubygem-rake
Provides:           ruby(runtime_executable)

%description
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard. mruby can be linked and embedded within your application.
We provide the interpreter program "mruby" and the interactive mruby shell
"mirb" as examples.

You can also compile Ruby programs into compiled byte code using the mruby
compiler "mrbc". The "mrbc" is also able to generate compiled byte code in a C
source file.

%package devel
Summary:            Lightweight Ruby Embedded Environment
Group:              Development/Languages/Ruby

%description devel
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard.

This package contains the headers and static library files in order to embed
mruby into your application.

%prep
%setup -q

%build
rake

%install
for b in mirb mrbc mruby; do
    %__install -Dm755 build/host/bin/"$b" "%{buildroot}%{_bindir}/$b"
done
for l in libmruby.a libmruby_core.a; do
    %__install -Dm644 build/host/lib/"$l" "%{buildroot}%{_libdir}/$l"
done
install -d "%{buildroot}%{_includedir}"
cp -a include/* "%{buildroot}%{_includedir}/"

%files
%doc AUTHORS LEGAL NEWS *.md LICENSE doc/*
%{_bindir}/mirb
%{_bindir}/mrbc
%{_bindir}/mruby
%{_bindir}/mrbc

%files devel
%{_includedir}/*.h
%{_includedir}/mruby
%{_libdir}/libmruby.a
%{_libdir}/libmruby_core.a

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
* Tue Jul  3 2012 pascal.bleser@opensuse.org
- initial version (0.0+20120701)
