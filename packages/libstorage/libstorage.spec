#
# spec file for package libstorage
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libstorage
Version:        2.26.12
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         libstorage-%{version}.tar.bz2

Prefix:         /usr

BuildRequires:  boost-devel
BuildRequires:  dejagnu
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  python-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig

Summary:        Library for storage management
License:        GPL-2.0
Group:          System/Libraries
Url:            http://en.opensuse.org/Portal:Libstorage

%description
This package contains libstorage, a library for storage management.

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?py_requires: %global py_requires Requires: python}

%if 0%{?ruby_sitelib} == 0
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%{!?ruby_sitelib: %global ruby_sitelib %(ruby -r rbconfig -e 'vd = Config::CONFIG["vendorlibdir"]; print(vd ? vd : Config::CONFIG["sitelibdir"])')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -r rbconfig -e 'vad = Config::CONFIG["vendorarchdir"]; print(vad ? vad : Config::CONFIG["sitearchdir"])')}
%{!?ruby_vendor: %global ruby_vendor %(ruby -r rbconfig -e 'vad = Config::CONFIG["vendor"]; print(vad ? vad : Config::CONFIG["vendor"])')}
%endif
%endif

%prep
%setup -n libstorage-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
export CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

aclocal
libtoolize --force --automake --copy
autoheader
automake --add-missing --copy
autoconf

%{?suse_update_config:%{suse_update_config -f}}
%if 0%{?fedora_version} || 0%{?centos_version}
CXXFLAGS="-I/usr/include/libxml2" \
%else
%if 0%{?rhel_version} >= 500 && 0%{?rhel_version} < 600
CXXFLAGS="-I/usr/include/libxml2 -I/usr/include/c++/4.1.1/tr1" \
%endif
%endif

./configure --libdir=%{_libdir} --prefix=%{prefix} --mandir=%{_mandir} --disable-silent-rules
make %{?jobs:-j%jobs}

%ifarch s390 s390x
sed -i -e 's/DEVICE_NAMES=".*"/DEVICE_NAMES="path"/' data/sysconfig.storage-libstorage
%endif

%check
%if ! 0%{?qemu_user_space_build}
LOCALEDIR=$RPM_BUILD_ROOT/usr/share/locale make check
%endif

%install
make install DESTDIR="$RPM_BUILD_ROOT"

install -d -m 755 $RPM_BUILD_ROOT/run/libstorage
touch $RPM_BUILD_ROOT/run/libstorage/lock

%{find_lang} libstorage

rm -f $RPM_BUILD_ROOT/%{python_sitearch}/_storage.a
rm -f $RPM_BUILD_ROOT/%{python_sitearch}/_storage.la
%if 0%{?suse_version}
%if "%{?rb_vendorarchdir}" != ""
rm -f $RPM_BUILD_ROOT/%{rb_vendorarchdir}/storage.la
%else
rm -f $RPM_BUILD_ROOT/%{rb_vendorarch}/storage.la
%endif
%endif
%if 0%{?mandriva_version}
rm $RPM_BUILD_ROOT/%{ruby_sitearchdir}/storage.la
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
rm $RPM_BUILD_ROOT/%{ruby_sitearch}/storage.la
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%package -n libstorage7

Requires:       coreutils
Suggests:       cryptsetup
Requires:       device-mapper
Suggests:       dmraid
Requires:       grep
Requires:       lsscsi >= 0.26
Suggests:       lvm2
Suggests:       mdadm >= 3.3
Suggests:       multipath-tools
Requires:       parted >= 3.1
Requires:       udev
Requires:       util-linux >= 2.16
%ifarch s390 s390x
Requires:       s390-tools
%endif

%if 0%{?suse_version}
PreReq:         %fillup_prereq
%endif
Obsoletes:      yast2-storage-lib
# expands to Obsoletes: libstorage libstorage1 libstorage2 libstorage3...
Obsoletes:      libstorage7 < %{version}
Obsoletes:      libstorage %(echo `seq -s " " -f "libstorage%.f" $((7 - 1))`)
Summary:        Library for storage management
Group:          System/Libraries

%description -n libstorage7
This package contains libstorage, a library for storage management.

Authors:
--------
    Thomas Fehr <fehr@suse.de>
    Arvin Schnell <aschnell@suse.de>

%files -n libstorage7 -f libstorage.lang
%defattr(-,root,root)
%{_libdir}/libstorage.so.*
%ghost /run/libstorage
/var/adm/fillup-templates/sysconfig.storage-libstorage
%doc %dir %{prefix}/share/doc/packages/libstorage
%doc %{prefix}/share/doc/packages/libstorage/AUTHORS
%doc %{prefix}/share/doc/packages/libstorage/COPYING

%post -n libstorage7
/sbin/ldconfig
%if 0%{?suse_version}
%{fillup_only -an storage}
%endif

%postun -n libstorage7
/sbin/ldconfig

%package -n libstorage-devel

Requires:       gcc-c++
Requires:       libstdc++-devel
Requires:       libstorage7 = %version
Requires:       libxml2-devel
Summary:        Header files and documentation for libstorage
Group:          Development/Languages/C and C++

%description -n libstorage-devel
This package contains header files and documentation for developing with
libstorage.

Authors:
--------
    Thomas Fehr <fehr@suse.de>
    Arvin Schnell <aschnell@suse.de>

%files -n libstorage-devel
%defattr(-,root,root)
%{_libdir}/libstorage.la
%{_libdir}/libstorage.so
%{prefix}/include/storage
%doc %{prefix}/share/doc/packages/libstorage/autodocs
%doc %{prefix}/share/doc/packages/libstorage/examples

%package -n libstorage-python

Requires:       libstorage7 = %version
%{py_requires}
Summary:        Python bindings for libstorage
Group:          System/Libraries

%description python
This package contains Python bindings for libstorage.

Authors:
--------
    Arvin Schnell <aschnell@suse.de>

%files -n libstorage-python
%defattr(-,root,root)
%{python_sitelib}/storage.py*
%attr(755,root,root) %{python_sitearch}/_storage.so

%package -n libstorage-ruby

Requires:       libstorage7 = %version
Summary:        Ruby bindings for libstorage
Group:          System/Libraries

%description ruby
This package contains Ruby bindings for libstorage.

Authors:
--------
    Thomas Fehr <fehr@suse.de>
    Arvin Schnell <aschnell@suse.de>

%files -n libstorage-ruby
%defattr(-,root,root)
%if 0%{?suse_version}
%if "%{?rb_vendorarchdir}" != ""
%{rb_vendorarchdir}/storage.so
%else
%{rb_vendorarch}/storage.so
%endif
%endif
%if 0%{?mandriva_version}
%{ruby_sitearchdir}/storage.so
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
%{ruby_sitearch}/storage.so
%endif

%package -n libstorage-testsuite

Requires:       libstorage7 = %version
Summary:        Testsuite for libstorage
Group:          Development/Tools/Other

%description -n libstorage-testsuite
This package contains testsuite programs for libstorage.

Authors:
--------
    Arvin Schnell <aschnell@suse.de>

%files testsuite
%defattr(-,root,root)
%dir /usr/lib/libstorage
/usr/lib/libstorage/testsuite-real

%changelog