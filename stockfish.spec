Name:           stockfish
Version:        5
Release:        6.1
Summary:        A chess engine
License:        GPLv3
Group:          Games/Boards
URL:            http://www.stockfishchess.com
Source0:        stockfish-5-src.zip
Source1:        stockfish-231-book.zip
Patch0:         %{name}-adjust-opening-book.patch
BuildRequires:  gcc-c++

%description
Stockfish is a free UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard
with PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz)
in order to be used comfortably. Read the documentation for your GUI of choice
for information about how to use Stockfish with your GUI.

%prep
%setup -q -n %{name}-%{version}-src -a 1
%patch0 -p0

%build
cd src
%ifarch x86_64
make build ARCH=x86-64
%else
%ifarch %arm
make build ARCH=arm-32
%else
make build ARCH=x86-32
%endif
%endif

%install
install -D -m0755 src/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m0644 logo.bmp %{buildroot}%{_datadir}/%{name}
install -m0644 polyglot.ini Book.bin %{buildroot}%{_datadir}/%{name}

%files
%doc Readme.md Copying.txt
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Oct 31 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 5
- Rebuild for Fedora
* Sun Dec 02 2012 kamil <kamil> 2.3.1-1.mga3
+ Revision: 324781
- new version 2.3.1
- rediff djust-opening-book.patch
* Wed Jul 25 2012 kamil <kamil> 2.2.2-1.mga3
+ Revision: 274391
- imported package stockfish
