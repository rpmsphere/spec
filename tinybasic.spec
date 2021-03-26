Summary: TinyBasic interpreter in C
Name: tinybasic
Version: 2006.1
Release: 3.1
License: CC0
Group: Development/Language
URL: http://www.ittybittycomputers.com/IttyBitty/TinyBasic/
Source0: http://www.ittybittycomputers.com/IttyBitty/TinyBasic/TinyBasic.c
Source1: http://www.ittybittycomputers.com/IttyBitty/TinyBasic/TBuserMan.txt

%description
In 1976 at the HomeBrew Computer Club (HBCC), there was a lot of whining about
Bill Gates charging $150 for his Basic interpreter. Dennis Allison responded
by printing a "Build Your Own [tiny] Basic" article, so Tom Pittman asked if
anybody would buy it if it cost only $5. There seemed to be some affirmation,
so Tom Pittman wrote his interpreter.

He also rewrote the original IttyBitty TinyBasic interpreter in C, translated
for modern enthusiasts. An accompanying article is published in the January
2006 issue of Dr.Dobb's Journal, p.24.

%prep
%setup -T -c
cp %{SOURCE0} %{SOURCE1} .

%build
gcc %{optflags} TinyBasic.c -o %{name}

%install
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%doc TBuserMan.txt
%{_bindir}/%{name}

%changelog
* Sun Dec 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2006.1
- Rebuild for Fedora
