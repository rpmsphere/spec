Name: crystal
Summary: Fast as C, Slick as Ruby
Version: 0.27.2
Release: 1
Group: Development/Languages
License: Apache License
URL: https://crystal-lang.org/
Source0: https://github.com/crystal-lang/crystal/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: libevent-devel
BuildRequires: pcre-devel

%description
Crystal is a programming language with the following goals:
* Have a syntax similar to Ruby (but compatibility with it is not a goal)
* Statically type-checked but without having to specify the type of variables or method arguments.
* Be able to call C code by writing bindings to it in Crystal.
* Have compile-time evaluation and generation of code, to avoid boilerplate code.
* Compile to efficient native code.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc *.md LICENSE
%{_bindir}/%{name}
%{_bindir}/shards
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/licenses/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Oct 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.26.1
- Rebuild for Fedora
