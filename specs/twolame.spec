Summary: Optimised MPEG Audio Layer 2 (MP2) encoder
Name: twolame
Version: 0.3.12
Release: 2%{?dist}
License: LGPLv2
Group: Applications/Multimedia
URL: http://www.twolame.org/
Source: http://dl.sf.net/twolame/twolame-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libsndfile-devel

%description
TwoLAME is an optimised MPEG Audio Layer 2 (MP2) encoder based on tooLAME by
Mike Cheng, which in turn is based upon the ISO dist10 code and portions of
LAME.


%package devel
Summary: Development files for TwoLAME
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
TwoLAME is an optimised MPEG Audio Layer 2 (MP2) encoder based on tooLAME by
Mike Cheng, which in turn is based upon the ISO dist10 code and portions of
LAME.


%prep
%setup -q
# Avoid standard rpaths on lib64 archs
sed -i -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure


%build
%configure --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Move docs back here to be included in the devel sub-package
%{__mv} %{buildroot}%{_docdir}/twolame/ _doc


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO 
%{_bindir}/twolame
%{_libdir}/libtwolame.so.*
%{_mandir}/man1/twolame.1*

%files devel
%defattr(-, root, root, 0755)
%doc _doc/* doc/html/
%{_includedir}/twolame.h
%{_libdir}/pkgconfig/twolame.pc
%exclude %{_libdir}/libtwolame.la
%{_libdir}/libtwolame.so


%changelog
* Sat Feb 08 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.3.12-2
- Removed rpath.

* Sun Jan 27 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.3.12-1
- Updated to release 0.3.12.

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 0.3.10-1
- Updated to release 0.3.10.

* Wed Jan 10 2007 Matthias Saou <http://freshrpms.net/> 0.3.9-1
- Initial RPM release.
