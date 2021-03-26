Name:          info2man
Version:       1.1.1
Release:       7.1
Summary:       Tool to convert GNU info documents into manual pages
Group:         Development/Tools
URL:           http://www.cskk.ezoshosting.com/cs/css/info2pod.html
Source:        http://www.cskk.ezoshosting.com/cs/css/info2man.tar.gz
Patch0:        %{name}-1.1.1-mktemp.patch
Patch1:        %{name}-1.1.1-makefile.patch
Patch2:        %{name}-1.1.1-manpages.patch
License:       OSI Approved
Requires:      perl
BuildRequires: perl-devel
BuildArch:     noarch

%description
info2man converts a GNU info file to a man page.
It first generates a POD (Plain Old Documentation) file using info2pod,
then converts this to a man page using pod2man.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

packlist=`find $RPM_BUILD_ROOT -name .packlist`
[ -z "$packlist" ] && exit 1 || cat $packlist | \
   sed "s,%buildroot,,g;s,.*/man/.*,&.gz,g" | \
   sort -u > .packlist && rm $packlist

strid=`echo $packlist | sed 's,.*auto\(.*\)/.packlist,\1,'`
for dir in `find $RPM_BUILD_ROOT -type d | grep $strid`; do
   echo "%dir ${dir#%buildroot}" >> .packlist
done

install -D -m 755 info2man $RPM_BUILD_ROOT%{_bindir}/info2man
install -m 755 info2pod  $RPM_BUILD_ROOT%{_bindir}/info2pod

install -D -m 644 info2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/info2man.1
install -m 644 info2pod.1 $RPM_BUILD_ROOT%{_mandir}/man1/info2pod.1

%clean
rm -rf $RPM_BUILD_ROOT
rm -f .packlist

%files -f .packlist
%{_bindir}/info2man
%{_bindir}/info2pod
%{_mandir}/man1/info2man.*
%{_mandir}/man1/info2pod.*
%doc LICENSE
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuild for Fedora
* Wed May 20 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.1.1-2mamba
- updated specfile
* Thu May 18 2006 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 1.1.1-1qilnx
- package created by autospec
