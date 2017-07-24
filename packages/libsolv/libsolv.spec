#
# spec file for package libsolv
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


Name:           libsolv
Version:        0.6.28
Release:        0
Url:            https://github.com/openSUSE/libsolv
Source:         libsolv-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%bcond_without enable_static
%bcond_without disable_shared
%bcond_without perl_binding
%bcond_without python_binding
%bcond_without python3_binding
%bcond_without ruby_binding
%bcond_with zypp

%if 0%{?leap_version} >= 420300 || 0%{?sle_version} >= 120300 || 0%{?suse_version} >= 1330 || !0%{?suse_version}
%bcond_without bz2
%bcond_without xz
%else
%bcond_with bz2
%bcond_with xz
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7 || 0%{?mageia} >= 6 || 0%{?suse_version} >= 1330
%bcond_without richdeps
%else
%bcond_with richdeps
%endif

%if 0%{?mandriva_version}
# force this version on mandriva
BuildRequires:  libneon0.26-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
BuildRequires:  db-devel
%endif
BuildRequires:  libxml2-devel
%if 0%{?suse_version} && 0%{?suse_version} < 1100
BuildRequires:  graphviz
%endif
%if 0%{?suse_version} > 1020 || 0%{?fedora} || 0%{?mageia}
BuildRequires:  fdupes
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rpm-devel
BuildRequires:  zlib-devel

%if %{with perl_binding}
BuildRequires:  perl
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
BuildRequires:  perl-devel
%endif
BuildRequires:  swig
%endif

%if %{with ruby_binding}
%global ruby_vendorarch %(ruby  -r rbconfig -e "puts RbConfig::CONFIG['vendorarchdir'].nil? ? RbConfig::CONFIG['sitearchdir'] : RbConfig::CONFIG['vendorarchdir']")
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig
%endif

%if %{with python_binding}
%global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True))")
BuildRequires:  python-devel
BuildRequires:  swig
%endif

%if %{with python3_binding}
%global python3_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True))")
BuildRequires:  python3-devel
%endif

%if %{with bz2}
%if 0%{?suse_version}
BuildRequires:  libbz2-devel
%else
BuildRequires:  bzip2-devel
%endif
%endif

%if %{with xz}
BuildRequires:  xz-devel
%endif

Summary:        A new approach to package dependency solving
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++

%description
A new approach to package dependency solving

%if !%{with disable_shared}
%package -n libsolv0
Summary:        A new approach to package dependency solving
Group:          Development/Libraries/C and C++

%description -n libsolv0
A new approach to package dependency solving

%endif
%package devel
Summary:        A new approach to package dependency solving
Group:          Development/Libraries/C and C++
%if !%{with disable_shared}
Requires:       libsolv0 = %version
%endif
Requires:       rpm-devel
Conflicts:      libsatsolver-devel

%description devel
Development files for libsolv, a new approach to package dependency solving

%package tools
Summary:        A new approach to package dependency solving
Group:          Development/Libraries/C and C++
Obsoletes:      satsolver-tools < 0.18
Provides:       satsolver-tools = 0.18
Conflicts:      satsolver-tools-obsolete
Requires:       bzip2
Requires:       coreutils
Requires:       findutils
Requires:       gzip

%description tools
A new approach to package dependency solving.

%package demo
Summary:        Applications demoing the libsolv library
Group:          System/Management
Requires:       curl
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mageia}
Requires:       gnupg2
%endif
%if 0%{?suse_version}
Requires:       gpg2
%endif
Conflicts:      libsatsolver-demo

%description demo
Applications demoing the libsolv library.

%package -n ruby-solv
Summary:        Ruby bindings for the libsolv library
Group:          Development/Languages/Ruby

%description -n ruby-solv
Ruby bindings for sat solver.

%package -n python-solv
%if 0%{?py_requires:1} && %{with python_binding}
%py_requires
%endif
Summary:        Python bindings for the libsolv library
Group:          Development/Languages/Python

%description -n python-solv
Python bindings for sat solver.

%package -n python3-solv
Summary:        Python3 bindings for the libsolv library
Group:          Development/Languages/Python

%description -n python3-solv
Python3 bindings for sat solver.

%package -n perl-solv
Requires:       perl = %{perl_version}
Summary:        Perl bindings for the libsolv library
Group:          Development/Languages/Perl

%description -n perl-solv
Perl bindings for sat solver.

%prep
%setup -n libsolv-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"

CMAKE_FLAGS=
%if 0%{?fedora} || 0%{?rhel} >= 6
CMAKE_FLAGS="-DFEDORA=1 -DENABLE_APPDATA=1 -DENABLE_COMPS=1"
%endif
%if 0%{?mageia}
CMAKE_FLAGS="-DMAGEIA=1 -DENABLE_APPDATA=1 -DENABLE_COMPS=1"
%endif
%if 0%{?suse_version}
CMAKE_FLAGS="-DSUSE=1 -DENABLE_APPDATA=1 -DENABLE_COMPS=1"
%endif

cmake	$CMAKE_FLAGS \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB=%{_lib} \
	-DCMAKE_VERBOSE_MAKEFILE=TRUE \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DWITH_LIBXML2=1 \
	%{?with_enable_static:-DENABLE_STATIC=1} \
	%{?with_disable_shared:-DDISABLE_SHARED=1} \
	%{?with_perl_binding:-DENABLE_PERL=1} \
	%{?with_python_binding:-DENABLE_PYTHON=1} \
	%{?with_python3_binding:-DENABLE_PYTHON3=1} \
	%{?with_ruby_binding:-DENABLE_RUBY=1} \
	%{?with_bz2:-DENABLE_BZIP2_COMPRESSION=1} \
	%{?with_xz:-DENABLE_LZMA_COMPRESSION=1} \
	%{?with_richdeps:-DENABLE_COMPLEX_DEPS=1} \
	%{?with_zypp:-DENABLE_SUSEREPO=1 -DENABLE_HELIXREPO=1} \
	-DUSE_VENDORDIRS=1 \
	-DCMAKE_SKIP_RPATH=1
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%if 0%{?suse_version}
%if %{with python_binding}
pushd $RPM_BUILD_ROOT/%{python_sitearch}
python %py_libdir/py_compile.py *.py
python -O %py_libdir/py_compile.py *.py
popd
%endif
%if %{with python3_binding}
%py3_compile $RPM_BUILD_ROOT/%{python3_sitearch}
%endif
%endif
%if %{with disable_shared}
# we want to leave the .a file untouched
export NO_BRP_STRIP_DEBUG=true
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%if !%{with disable_shared}
%post -n libsolv0 -p /sbin/ldconfig

%postun -n libsolv0 -p /sbin/ldconfig

%files -n libsolv0
%defattr(-,root,root)
%doc LICENSE*
%{_libdir}/libsolv.so.*
%{_libdir}/libsolvext.so.*
%endif

%files tools
%defattr(-,root,root)
%if 0%{?suse_version}
%exclude %{_bindir}/helix2solv
%exclude %{_mandir}/man1/helix2solv*
%endif
%exclude %{_bindir}/solv
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%if %{with enable_static}
%{_libdir}/libsolv.a
%{_libdir}/libsolvext.a
%endif
%if !%{with disable_shared}
%{_libdir}/libsolv.so
%{_libdir}/libsolvext.so
%endif
%{_includedir}/solv
%if 0%{?suse_version}
%{_bindir}/helix2solv
%{_mandir}/man1/helix2solv*
%endif
%{_datadir}/cmake/Modules/*
%{_libdir}/pkgconfig/libsolv*.pc
%{_mandir}/man3/*

%files demo
%defattr(-,root,root)
%{_bindir}/solv

%if %{with perl_binding}
%files -n perl-solv
%defattr(-,root,root)
%{perl_vendorarch}/*
%endif

%if %{with ruby_binding}
%files -n ruby-solv
%defattr(-,root,root)
%{ruby_vendorarch}/*
%endif

%if %{with python_binding}
%files -n python-solv
%defattr(-,root,root)
%{python_sitearch}/*
%endif

%if %{with python3_binding}
%files -n python3-solv
%defattr(-,root,root)
%{python3_sitearch}/*solv*
%if 0%{?suse_version}
%{python3_sitearch}/*/*solv*
%endif
%endif

%changelog
