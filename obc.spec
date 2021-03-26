Name: obc
Summary: Oxford Oberon-2 compiler
Version: 3.1.1
Release: 1
Group: Development/Language
License: Free Software
URL: https://github.com/Spivoxity/obc-3
Source0: %{name}-3-rel-%{version}.tar.gz
BuildRequires: ocaml
BuildRequires: tcl
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk2-devel
BuildRequires: gtksourceview2-devel
BuildRequires: pango-devel

%description
This compiler translates Oberon-2 into a portable bytecode, and comes
with an interpreter (or on some architecures, a JIT) for the bytecode.

%prep
%setup -q -n %{name}-3-rel-%{version}
#sed -i 's| sanity||' Makefile.in
sed -i -e 's|young_start|Caml_state_field(young_start)|' -e 's|young_end|Caml_state_field(young_end)|' lablgtk/ml_gpointer.c
sed -i -e 's|caml_young_start|Caml_state_field(young_start)|' -e 's|caml_young_end|Caml_state_field(young_end)|' lablgtk/ml_gtktree.c

%build
autoreconf
%configure
sed -i 's|ocamlc |ocamlc -cclib -Wl,--allow-multiple-definition |' Makefile */Makefile
make %{?_smp_mflags}

%install
sed -i -e 's|dir = /usr|dir = ${DESTDIR}/usr|' -e 's|@MODULES@||' Makefile
make install DESTDIR=%{buildroot}

%files
%doc README THANKS
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/*.1.*

%changelog
* Mon Sep 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.1
- Rebuild for Fedora
