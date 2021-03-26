Name: mosesdecoder
Summary: Decoder for the machine translation system
Version: 4.0
Release: 6.1
Group: Applications/Engineering
License: LGPL
URL: http://www.statmt.org/moses/
Source0: %{name}-master.zip
BuildRequires: jam
BuildRequires: boost-devel

%description
Moses is a statistical machine translation system that allows you to
automatically train translation models for any language pair. All you
need is a collection of translated texts (parallel corpus). An efficient
search algorithm finds quickly the highest probability translation among
the exponential number of choices.

%prep
%setup -q -n %{name}-master

%build
./bjam --no-xmlrpc-c

%install
mkdir -p %{buildroot}%{_bindir}
cp -a bin/* %{buildroot}%{_bindir}

%files
%doc BUILD-INSTRUCTIONS.txt
%{_bindir}/*

%changelog
* Thu Nov 09 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0
- Rebuild for Fedora