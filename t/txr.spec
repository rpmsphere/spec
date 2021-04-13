Name: txr
Summary: A Pattern Matching Language (Not Just) for Convenient Text Extraction
Version: 256
Release: 1
Group: Development/Languages
License: BSD
URL: http://www.nongnu.org/txr/
Source0: http://www.kylheku.com/cgit/txr/snapshot/txr-%{version}.tar.bz2
BuildRequires: flex-devel

%description
TXR is a fusion of different streams of thought. It is influenced by concepts
from text processing languages such as awk or perl, pattern matching concepts
from logic/AI programming, Lisp and functional languages. It is relatively new.
Development began around September 2009.

%prep
%setup -q

%build
%ifarch aarch64
export CC=clang CXX=clang++
%endif
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc ChangeLog* HACKING LICENSE RELNOTES
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 256
- Rebuild for Fedora
