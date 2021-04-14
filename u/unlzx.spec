Summary:	Unarchiver for Amiga LZX archives
Name:		unlzx
Version:	1.1
Release:	4.1
License:	distributable
Group:		Applications/Archiving
Source0:	http://aminet.net/misc/unix/unlzx.c.gz
Source1:	http://aminet.net/misc/unix/unlzx.c.gz.readme
URL:		http://xavprods.free.fr/lzx/

%description
LZX uses a compact way of encoding large match offsets. The Amiga
implementation includes file merging, where data are grouped into
large blocks, instead of being individually compressed.

%prep
%setup -q -T -c
gunzip %{SOURCE0} -c > %{name}.c
cp %{SOURCE1} README

%build
gcc %{optflags} -o %{name} %{name}.c

%install
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/*

%changelog
* Sun Sep 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
