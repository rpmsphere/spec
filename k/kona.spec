Name: kona
Summary: Open-source implementation of the K programming language
Version: 3.2.0
Release: 1
Group: Development/Language
License: ISC
URL: https://github.com/kevinlawler/kona
Source0: %{name}-master.zip

%description
Kona is the open-source implementation of the K programming language. K is
a synthesis of APL and LISP. Although many of the capabilities come from APL,
the fundamental data construct is quite different. In APL the construct is
a multi-dimensional matrix-like array, where the dimension of the array can
range from 0 to some maximum (often 9). In K, like LISP, the fundamental data
construct is a list. Also, like LISP, the K language is ASCII-based, so you
don't need a special keyboard.

%prep
%setup -q -n %{name}-master
sed -i -e '/if(b)boilerplate();/d' -e '98i if(b)boilerplate();' src/kc.c

%build
export CC="gcc -Wl,--allow-multiple-definition"
make

%install
install -Dm755 k %{buildroot}%{_bindir}/%{name}

%files
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0
- Rebuild for Fedora
